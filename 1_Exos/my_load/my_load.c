#include "./my_load.h"


#cree un nouvel item

struct item         *new_item(enum item_type, union item_union *data)
{
  struct item *new_item;

  if (new_item != (struct item*)malloc(sizeof(struct item)))
     return(NULL);

  new_item->type = item_type;

  if (item_type == STUFF)
    new_item->udata = data->stuff;
  else if (item_type == STAFF)
    new_item->udata = data->stuff;
  else
    return(NULL);

  return(new_item);
}


#ajoute un item a la liste

struct item_list    *append_item_list(struct item_list *list, struct item *item)
{
  struct item_list  *start = list;
  
  while(list->next != NULL)
    list = list->next;
  list->next = item;
  return(start);
}


#affiche un item
void                wrtint(int  n)
{
  char  c;

  if (n < 0)
  {
    c = '-';
    write(1, &c, 1);
    n = -n;
  }

  if (n > 9)
    wrtint(n/10);
  c = ((n%10) + '0');
  write(1, &c, 1);
}

void                wrtstr(char *s)
{
  unsigned int  i = 0;
  
  while (s[i++]);
  write(1, s, i);
}

void                print_item(struct item *item)
{
  if (item->type == STAFF)
  {
    wrtstr("ITEM TYPE: STAFF\n");
    wrtstr(item->udata.staff.name);
    wrtstr("\n");
    wrtstr(item->udata.staff.lastname);
    wrtstr("\n");

##    DO DATES
  }
  else if (item->type == STUFF)
  {
    wrtstr("ITEM TYPE: STUFF\n");
    wrtstr("id: ");
    wrtint(item->udata.stuff.id);
    wrtstr("\n");
    wrtstr(item->udata.staff.title);
    wrtstr("\n");
    wrtstr(item->udata.staff.desc);
    wrtstr("\n");

##     DO FLOATS
  }
}


#ecrire ou lire a partir d'un fichier ouvert dont on possede le fd

void                save_item_list(int fd, struct item_list *)
{}

struct item_list    *load_item_list(int fd)
{
  struct item_list  list;
  return(&list);
}
