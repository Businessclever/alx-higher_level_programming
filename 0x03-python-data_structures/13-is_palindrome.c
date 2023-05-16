#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *mid = NULL;

	/* Find the middle of the linked list */
	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	/* If the length of the list is odd, move slow one step forward */
	if (fast)
	{
		mid = slow;
		slow = slow->next;
	}

	/* Reverse the second half of the list */
	reverse_listint(&slow);

	/* Compare the reversed second half with the first half */
	while (slow)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}

	/* Restore the original list by reversing the reversed second half */
	if (mid)
		reverse_listint(&(mid->next));

	return (1);
}

