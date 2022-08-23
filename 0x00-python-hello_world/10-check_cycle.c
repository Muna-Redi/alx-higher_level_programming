#include "lists.h"

/**
 * check_cycle - checks if a linked list is a cycle
 * @list: list to be checked
 * Return: 1 (linked list is a cycle) 0 (not a cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *fast = NULL;

	slow = fast = list;
	if (slow == NULL)
		return (0);
	while (slow->next && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (!slow || !fast)
			return (0);
		if (fast->next == slow)
			return (1); 
	}
	return (0);
}
