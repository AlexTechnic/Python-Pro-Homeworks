""" Module of group class errors """


class GroupLimitError(Exception):
    def __init__(self, max_members, title):
        self.max_members = max_members
        self.title = title

    def __str__(self):
        return f'In group "{self.title}" are already {self.max_members} members.'


class SameMemberError(Exception):
    def __init__(self, member, group_title):
        self.member = member
        self.group_title = group_title

    def __str__(self):
        return f'Member {self.member}, already registered in group "{self.group_title}".'
