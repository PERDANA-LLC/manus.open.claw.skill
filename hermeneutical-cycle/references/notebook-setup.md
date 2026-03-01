# NotebookLM Setup for the Hermeneutical Cycle

To get the most out of the Hermeneutical Cycle skill, set up NotebookLM notebooks using the Thematic Canon Architecture.

## Recommended Notebook Structure

| Notebook | Books | Topics Tag |
|----------|-------|------------|
| 01-Pentateuch | Genesis, Exodus, Leviticus, Numbers, Deuteronomy | Pentateuch,Law,Moses,Genesis,Exodus,Leviticus,Numbers,Deuteronomy |
| 02-Historical | Joshua, Judges, Ruth, 1-2 Samuel, 1-2 Kings, 1-2 Chronicles, Ezra, Nehemiah, Esther | Historical,Israel,Joshua,Judges,Samuel,Kings,Chronicles |
| 03-Poetry-Wisdom | Job, Psalms, Proverbs, Ecclesiastes, Song of Solomon | Poetry,Wisdom,Psalms,Proverbs,Job,Ecclesiastes |
| 04-Major-Prophets | Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel | Prophets,Major,Isaiah,Jeremiah,Ezekiel,Daniel |
| 05-Minor-Prophets | Hosea through Malachi | Prophets,Minor,Hosea,Joel,Amos,Obadiah,Jonah,Micah,Nahum,Habakkuk,Zephaniah,Haggai,Zechariah,Malachi |
| 06-Gospels-Acts | Matthew, Mark, Luke, John, Acts | Gospels,Acts,Jesus,Christ,Matthew,Mark,Luke,John |
| 07-Pauline-Epistles | Romans through Philemon | Paul,Epistles,Romans,Corinthians,Galatians,Ephesians,Philippians,Colossians,Thessalonians,Timothy,Titus,Philemon |
| 08-General-Epistles | Hebrews, James, 1-2 Peter, 1-3 John, Jude | General,Epistles,Hebrews,James,Peter,John,Jude |
| 09-Apocalyptic | Revelation | Revelation,Apocalyptic,Prophecy,End Times |

## Sources to Upload Per Notebook

For each notebook, upload:
1. KJV text files for each book in the group (PDF or TXT)
2. Commentary files from your chosen commentators (e.g., Constable, Wiersbe, Stott, Ironside, Blackaby)
3. Optional: Strong's Concordance data for the relevant books

## Registering with Manus

After creating notebooks in NotebookLM, register each one:

```bash
cd /home/ubuntu/skills/notebooklm
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/[YOUR-URL]" \
  --name "[Notebook Name]" \
  --description "[What books and commentaries are included]" \
  --topics "[Comma-separated topic tags from table above]"
```

Verify with:
```bash
python scripts/run.py notebook_manager.py list
```
