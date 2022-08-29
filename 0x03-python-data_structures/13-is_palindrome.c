#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is palindrome
* @head: double pointer to head of the list
* Return: 0 if palindrome and 1 oif otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *tmp = NULL, *tmp2 = NULL;
	int *nums, i = 0, len;

	len = list_size(head);
	nums = malloc(sizeof(int *) * (len + 1));
	if (nums == NULL)
		return (1);
	tmp = tmp2 = *head;
	if (*head == NULL)
		return (1);
	while (tmp->next)
	{
		nums[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	nums[i] = tmp->n;
	while (i >= 0 && tmp2 != NULL)
	{
		if (tmp2->n == nums[i])
		{
			tmp2 = tmp2->next;
			i--;
			continue;
		}
		else
				return (0);
	}
		free(nums);
		return (1);
}
/**
* list_size - gets the size of a list
* @head: pointer to head of the list
* Return: size of the list
*/
int list_size(listint_t **head)
{
	listint_t *tmp = NULL;
	int i = 1;

	tmp = *head;
	if (*head == NULL)
		return (0);
	while (tmp)
	{
		tmp = tmp->next;
		i++;
	}
	return (i);
}
