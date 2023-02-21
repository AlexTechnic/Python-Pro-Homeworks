""" Module add group class that works with general humans instances, supporting managing of members """

import exceptions
import human


class Group:
    def __init__(self, title: str = 'Group title', max_members: int = 1):
        self.__title = title
        self.__max_members = max_members
        self.__members = []

    def get_max_members(self):
        """  'getter' of group max members limit """
        return {self.__max_members}

    def set_max_members(self, set_members):
        """ 'setter' of group max members limit """

        if not isinstance(set_members, int):
            raise TypeError()
        if set_members <= 0:
            raise ValueError()

        self.__max_members = set_members

    def get_title(self):
        """  'getter' of group title """
        return self.__title

    def set_title(self, new_title):
        """ 'setter' of group title """

        if not isinstance(new_title, str):
            raise TypeError()

        self.__title = new_title

    def add_member(self, member):
        if member in self.__members:
            raise exceptions.SameMemberError(member, self.__title)
        if len(self.__members) >= self.__max_members:
            raise exceptions.GroupLimitError(self.__max_members, self.__title)

        self.__members.append(member)

    def remove_member(self, member):
        if not isinstance(member, human.Human):
            raise TypeError()
        self.__members.remove(member)

    def search_members(self, search_item):
        """ in-group search method, return list with search query matches """

        result = []

        for member in self.__members:
            if search_item in str(member):
                result.append(str(member))
        return result

    def __str__(self):
        return f'\nGroup "{self.__title}" ' \
               f'include {len(self.__members)}/{self.__max_members} members\n\t' \
               + '\n\t'.join(map(str, self.__members)) + '\n'
