#include "lists.h"

/**
 * insert_node - inserts a node sorted in a linked list of ints
 * @head: double pointer to head of the list
 * @number: data for new node
 * Return: pointer to newly created node, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *new_node = NULL;

	if (!head)
		return (NULL);
	else if (!(*head))
	{
		new_node = make_node(number);
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current)
	{
		if (current->n >= number)
		{
			new_node = make_node(number);
			new_node->next = current;
			*head = new_node;
			return (new_node);
		}
		else if (current->n <= number)
		{
			if (!current->next || current->next->n >= number)
			{
				new_node = make_node(number);
				new_node->next = current->next;
				current->next = new_node;
				return (current->next);
			}
		}
		current = current->next;
	}
	return (NULL);
}


/**
 * make_node - creates a new node in the list
 * @n: data to be inserted in the new node
 * Return: pointer to newly allocated node
 */
listint_t *make_node(int n)
{
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->next = NULL;
	new->n = n;
	return (new);
	free(new);
}
