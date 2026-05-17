from pyTigerGraph.pyTigerGraph import TigerGraphConnection

conn = TigerGraphConnection(
    host="tg-569e8832-4ce5-46eb-a01f-58f4eef59305.tg-3452941248.i.tgcloud.io",
    graphname="booksgraph",
    apiToken="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzaGl2YW5naWt1bWFyMjAwN0BnbWFpbC5jb20iLCJpYXQiOjE3Nzg5MjkzMDAsImV4cCI6MTc3OTUzNDEwNSwiaXNzIjoiVGlnZXJHcmFwaCJ9.CBOVkHEWFczxW3gdCgvvr0XG9Qv-SUUgH8VJZY6qyE0"
)

print("TigerGraph Connected!")