// Welcome to Secure Code Game Season-1/Level-2!

// Follow the instructions below to get started:

// 1. Perform code review. Can you spot the bug? 
// 2. Run tests.c to test the functionality
// 3. Run hack.c and if passing then CONGRATS!
// 4. Compare your solution with solution.c

#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_USERNAME_LEN 39
#define SETTINGS_COUNT 10
#define MAX_USERS 100
#define INVALID_USER_ID -1

int userid_next = 0;

typedef struct {
    bool isAdmin;
    long userid;
    char username[MAX_USERNAME_LEN + 1];
    long setting[SETTINGS_COUNT];
} user_account;

user_account *accounts[MAX_USERS];


int create_user_account(bool isAdmin, const char *username) {
    if (userid_next >= MAX_USERS) {
        fprintf(stderr, "Error: Maximum number of users reached.\n");
        return INVALID_USER_ID;
    }

    if (username == NULL || strlen(username) > MAX_USERNAME_LEN) {
        fprintf(stderr, "Error: Invalid or too long username.\n");
        return INVALID_USER_ID;
    }

    user_account *ua = (user_account *)malloc(sizeof(user_account));
    if (ua == NULL) {
        fprintf(stderr, "Error: Memory allocation failed.\n");
        return INVALID_USER_ID;
    }

    ua->isAdmin = isAdmin;
    ua->userid = userid_next;
    strncpy(ua->username, username, MAX_USERNAME_LEN);
    ua->username[MAX_USERNAME_LEN] = '\0'; 
    memset(ua->setting, 0, sizeof(ua->setting));

    accounts[userid_next] = ua;
    return userid_next++;
}

bool update_setting(int user_id, const char *index, const char *value) {
    if (user_id < 0 || user_id >= MAX_USERS || accounts[user_id] == NULL) {
        fprintf(stderr, "Error: Invalid user ID.\n");
        return false;
    }

    char *endptr;
    long i = strtol(index, &endptr, 10);
    if (*endptr != '\0' || i < 0 || i >= SETTINGS_COUNT) {
        fprintf(stderr, "Error: Invalid setting index.\n");
        return false;
    }

    long v = strtol(value, &endptr, 10);
    if (*endptr != '\0') {
        fprintf(stderr, "Error: Invalid setting value.\n");
        return false;
    }

    if (!accounts[user_id]->isAdmin && i == SETTINGS_COUNT - 1) {
        fprintf(stderr, "Error: Non-admin users cannot modify this setting.\n");
        return false;
    }

    accounts[user_id]->setting[i] = v;
    return true;
}

bool is_admin(int user_id) {
    if (user_id < 0 || user_id >= MAX_USERS || accounts[user_id] == NULL) {
        fprintf(stderr, "Error: Invalid user ID.\n");
        return false;
    }
    return accounts[user_id]->isAdmin;
}

const char* username(int user_id) {
    if (user_id < 0 || user_id >= MAX_USERS || accounts[user_id] == NULL) {
        fprintf(stderr, "Error: Invalid user ID.\n");
        return NULL;
    }
    return accounts[user_id]->username;
}

void cleanup_users() {
    for (int i = 0; i < MAX_USERS; i++) {
        if (accounts[i] != NULL) {
            free(accounts[i]);
            accounts[i] = NULL;
        }
    }
}



