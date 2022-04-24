#
# import gitlab
#
#
# this_per_page = 90
# # this_total_pages = 100
# # nd = 1
#
#
#
# client = gitlab.Gitlab('http://x.x.x.x:8888/', private_token='xxxxxxxxxxxxxxx', api_version='4')
# client.auth()
# project = client.projects.list()
#
#
#
#
#
# # , per_page=this_per_page
# project = client.projects.list(as_list=False, per_page=this_per_page)
# # for p1 in project:
# #     print(project.total_pages)
# this_total_pages = project.total_pages
#
# total = []
# total_line = 0
#
#
#
#
#
# for p in range(this_total_pages):
#     # print("pppppppppp")
#     # print(p)
#     projects = client.projects.list(as_list=False, page=p+1, per_page=this_per_page)
#     for i, project in enumerate(projects):
#         print(i)
#         total.append(project.attributes)
#
#         commits_pages = project.commits.list(since='2020-01-01T00:00:00Z', as_list=False, per_page=this_per_page).total_pages
#         _thread
#         for pp in range(commits_pages):
#             commits = project.commits.list(since='2020-01-01T00:00:00Z', page=pp + 1, per_page=this_per_page)
#             for j, commit in enumerate(commits):
#                 _commit = project.commits.get(commit.id)
#                 total_line = total_line + _commit.stats['total']
#             print(total_line)
#
# print("total commit line: {0}".format(total_line))
#
#
#
# exit(0)