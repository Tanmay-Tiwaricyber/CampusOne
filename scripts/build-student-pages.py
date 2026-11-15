"""Generate the static student pages from templates/student.html. No dependencies."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
template = (root / 'templates/student.html').read_text(encoding='utf-8')
pages = {
    'overview': ('student.html', 'Student dashboard'),
    'profile': ('student-profile.html', 'Student profile'),
    'leave': ('student-leave.html', 'Leave requests'),
    'academics': ('student-academics.html', 'Academics'),
    'schedule': ('student-schedule.html', 'Timetable and notices'),
    'resources': ('student-resources.html', 'Resources'),
    'services': ('student-services.html', 'Campus services'),
}
pattern = re.compile(r'<!-- VIEW:([a-z]+):start -->(.*?)<!-- VIEW:\1:end -->', re.S)
for name, (filename, title) in pages.items():
    html = pattern.sub(lambda m: m.group(2) if m.group(1) == name else '', template)
    html = html.replace('{{PAGE}}', name).replace('{{TITLE}}', title)
    (root / filename).write_text(html, encoding='utf-8')
    print('Built', filename)
