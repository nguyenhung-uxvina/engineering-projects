# 📊 ENGINEERING DASHBOARD

## Active Projects by Phase

### Phase 1: Task Clarification
```dataview
TABLE status, next_action
FROM "vault/projects"
WHERE phase = 1
SORT file.mtime DESC
```

### Phase 2: Conceptual Design
```dataview
TABLE status, vdi_score
FROM "vault/projects"
WHERE phase = 2
SORT file.mtime DESC
```

## Recent Activity
```dataview
TABLE file.mtime as "Last Modified"
FROM "vault/projects"
SORT file.mtime DESC
LIMIT 10
```

## This Week's Learning
```dataview
LIST
FROM "vault/learning-journal/weekly"
WHERE file.ctime >= date(today) - dur(7 days)
```