CREATE TABLE IF NOT EXISTS skills (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  domain TEXT NOT NULL,
  description TEXT,
  prereqs_json TEXT NOT NULL,
  mastery_score REAL NOT NULL DEFAULT 0,
  last_practiced TEXT,
  target_mastery REAL NOT NULL DEFAULT 80
);
CREATE TABLE IF NOT EXISTS drill_questions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  domain TEXT NOT NULL,
  prompt TEXT NOT NULL,
  answer TEXT NOT NULL,
  difficulty REAL NOT NULL,
  tags_json TEXT NOT NULL,
  skill_ids_json TEXT NOT NULL,
  next_due TEXT,
  easiness REAL NOT NULL DEFAULT 2.5,
  interval INTEGER NOT NULL DEFAULT 1,
  repetitions INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS drill_reviews (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  question_id INTEGER NOT NULL,
  ts TEXT NOT NULL,
  correct INTEGER NOT NULL,
  response_time REAL NOT NULL,
  error_tags_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS sprints (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  template TEXT NOT NULL,
  hypothesis TEXT NOT NULL,
  dataset_ref TEXT,
  status TEXT NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS sprint_metrics (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  sprint_id INTEGER NOT NULL,
  metrics_json TEXT NOT NULL,
  passed_checks INTEGER NOT NULL,
  notes TEXT
);
CREATE TABLE IF NOT EXISTS artifacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  sprint_id INTEGER,
  path TEXT NOT NULL,
  created_at TEXT NOT NULL,
  kind TEXT NOT NULL,
  metadata_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS career_applications (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  company TEXT NOT NULL,
  role TEXT NOT NULL,
  status TEXT NOT NULL,
  date_applied TEXT NOT NULL,
  next_action TEXT,
  notes TEXT
);
CREATE TABLE IF NOT EXISTS career_contacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  org TEXT,
  last_contact TEXT,
  next_followup TEXT,
  notes TEXT
);
CREATE TABLE IF NOT EXISTS planner_semester (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  start_date TEXT NOT NULL,
  end_date TEXT NOT NULL,
  subjects_json TEXT NOT NULL,
  load_weight REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS settings (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);
