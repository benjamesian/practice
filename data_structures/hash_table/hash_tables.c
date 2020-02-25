#include "hash_tables.h"
#include <string.h>
#include <stdio.h>

/**
 * hash_table_create - Create a hash table.
 * @size: Size of array in the hash table.
 * 
 * Return: Pointer to newly created hash table on success, else NULL.
 */
hash_table_t *hash_table_create(size_t size)
{
    hash_table_t *ht = NULL;

    if (!size)
        return (NULL);

    ht = malloc(sizeof(*ht));
    if (!ht)
        return (NULL);
    ht->array = calloc(size, sizeof(*ht->array));
    if (!ht->array)
    {
        free(ht);
        return (NULL);
    }

    ht->size = size;

    return (ht);
}

/**
 * hash_djb2 - A hash function.
 * @str: String to create hash for.
 * 
 * Return: Hash for the string.
 */
unsigned long hash_djb2(const unsigned char *str)
{
    unsigned long hash = 5381;
    int c;

    while ((c = *str++))
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    return (hash);
}

/**
 * key_index - Get the index where a key should be stored in a hash table's internal array.
 * @key: Key to store.
 * @size: Size of internal hash table array.
 * 
 * Return: Index where key should be stored.
 */
size_t key_index(const unsigned char *key, size_t size)
{
    return (hash_djb2(key) % size);
}

/**
 * hash_node_free - Free the memory allocated for a node.
 * @p_node: Address of node pointer to free.
 */
void hash_node_free(hash_node_t **p_node)
{
    if (p_node && *p_node)
    {
        free((*p_node)->key);
        free((*p_node)->value);
        free(*p_node);
    }
}

/**
 * hash_node_update - Update the value held by a node.
 * @node: Node to update.
 * @value: New value.
 * 
 * Return: 1 if value was updated else 0.
 */
int hash_node_update(hash_node_t *node, const char *value)
{
    char *value_copy = NULL;

    if (!node)
        return (0);

    if (value)
    {
        value_copy = strdup(value);
        if (!value_copy)
            return (0);
        free(node->value);
        node->value = value_copy;
    }

    return (1);
}

/**
 * hash_node_create - Create a new hash node at the address p_node.
 * @p_node: Address where newly created node pointer will be stored.
 * @key: Key of the new node.
 * @value: Value of the new node.
 * 
 * Return: 1 if a new node was successfully created, else 0.
 */
int hash_node_create(hash_node_t **p_node, const char *key, const char *value)
{
    hash_node_t *new = calloc(1, sizeof(*new));

    if (!new)
        return (0);

    new->key = strdup(key);
    if (!new->key)
    {
        free(new);
        return (0);
    }

    if (!hash_node_update(new, value))
        hash_node_free(&new);

    *p_node = new;
    return (!!new);
}

/**
 * hash_table_set - Set a key-value pair in a hash table.
 * @ht: Hash table.
 * @key: Key in the key-value pair.
 * @value: Value in the key-value pair.
 * 
 * Return: 1 if a key-value pair was successfully set in the hash table, else 0.
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
    size_t ki;
    hash_node_t *p = NULL, *temp = NULL;

    if (!ht || !key || !*key || !value)
        return (0);

    ki = key_index(key, ht->size);
    p = ht->array[ki];
    if (!p)
        return (hash_node_create(&ht->array[ki], key, value));

    if (strcmp(key, p->key) == 0)
        return (hash_node_update(p, value));

    while (p->next && strcmp(key, p->next->key) != 0)
        p = p->next;

    if (!p->next)
        return (hash_node_create(&p->next, key, value));

    if (!hash_node_update(p->next, value))
        return (0);

    // put at front, might be accessed regularly
    temp = p->next;
    p->next = p->next->next;
    temp->next = ht->array[ki];
    ht->array[ki] = temp;

    return (1);
}

/**
 * hash_table_get - Get the value associated with a key in a hash table.
 * @ht: Hash table.
 * @key: Key to get associated value of.
 * 
 * Return: The value associated with `key` or NULL if there is no such value.
 */
char *hash_table_get(hash_table_t *ht, const char *key)
{
    hash_node_t *p = ht->array[key_index(key, ht->size)];

    while (p && strcmp(key, p->key) != 0)
        p = p->next;

    return (p ? p->value : NULL);
}

/**
 * hash_table_print - Print all elements stored in a hash table.
 * @ht: Hash table with elements to print.
 */
void hash_table_print(hash_table_t *ht)
{
    int comma_flag = 0;
    hash_node_t *p = NULL;

    if (!ht)
        return;

    putchar('{');
    for (size_t i = 0; i < ht->size; i++)
    {
        p = ht->array[i];
        while (p)
        {
            if (comma_flag)
                printf(", ");
            else
                comma_flag = 1;

            printf("%s: %s", p->key, p->value);
            p = p->next;
        }
    }
    printf("}\n");
}

/**
 * hash_table_delete - Free all memory allocated for a hash table.
 * @ht: Hash table to free.
 */
void hash_table_delete(hash_table_t *ht)
{
    hash_node_t *p = NULL, *temp = NULL;

    if (!ht)
        return;

    for (size_t i = 0; i < ht->size; i++)
    {
        p = ht->array[i];
        while (p)
        {
            temp = p;
            p = p->next;
            hash_node_free(&temp);
        }
    }

    free(ht->array);
    free(ht);
}
