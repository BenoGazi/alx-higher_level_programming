#include "lists.h"

/**
 * is_palindrome - checcks if a singly linked list is a palindrome
 * @head: head node
 * Return: 0 if npt a palindrome and 1 if it is
 * An empty list is considered a palindrome
 */

int is_palindrome(listint_t **head)
{
	int _len, i;
	listint_t *temp, *middle;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	temp = *head;
	_len = 0;
	while (temp)
	{
		temp = temp->next;
		_len++;
	}
	i = 0;
	middle = *head;
	while (i < _len / 2)
	{
		middle = middle->next;
		i++;
	}
	if (_len % 2 != 0)
	{
		middle = middle->next;
	}
	_rev(&middle);
	i = _listcomp(*head, middle, _len);
	return (i);
}

/**
 * _rev - reverses a linked list
 * @head: head node
 * Return: Nothing
 */

void _rev(listint_t **head)
{
	listint_t *current, *prev, *next;

	if (head == NULL || *head == NULL)
	{
		return;
	}
	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}


/**
 * _listcomp - compares lists
 * @head: head node
 * @middle: middle node
 * @_len: length of list
 * Return: Success
 */

int _listcomp(listint_t *head, listint_t *middle, int _len)
{
	int i;

	if (head == NULL || middle == NULL)
	{
		return (1);
	}
	i = 0;
	while (i < _len)
	{
		if (head->n != middle->n)
		{
			return (0);
		}
		head = head->next;
		middle = middle->next;
		i++;
	}
	return (1);
}
