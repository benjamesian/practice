#ifndef HASH_TABLES_H
#define HASH_TABLES_H

#include <stdlib.h>

typedef struct hash_node_s {
    char *key;
    char *value;
    struct hash_node_s *next;
} hash_node_t;

typedef struct hash_table_s {
    size_t size;
    hash_node_t **array;
} hash_table_t;

hash_table_t *hash_table_create(size_t size);
size_t hash_djb2(const unsigned char *str);
size_t key_index(const unsigned char *key, size_t size);
int hash_table_set(hash_table_t *ht, const char *key, const char *value);
char *hash_table_get(hash_table_t *ht, const char *key);
void hash_table_print(hash_table_t *ht);
void hash_table_delete(hash_table_t *ht);

#endif /* HASH_TABLES_H */
