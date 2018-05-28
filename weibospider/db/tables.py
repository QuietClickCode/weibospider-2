from sqlalchemy import (
    Table, Column, INTEGER, String, Text)

from .basic import metadata


__all__ = ['login_info', 'wbuser', 'seed_id',
           'keyword', 'wbdata', 'keyword_wbdata',
           'comment', 'repost', 'relation',
           'dialogue', 'praise', 'task_label']

# login table
login_info = Table("login_info", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("name", String(100), unique=True),
                   Column("password", String(200)),
                   Column("enable", INTEGER, default=1, server_default='1'),
                   )

wbuser = Table("wbuser", metadata,
               Column("id", INTEGER, primary_key=True, autoincrement=True),
               Column("uid", String(20), unique=True),
               Column("name", String(200), default='', server_default=''),
               Column("gender", INTEGER, default=0, server_default='0'),
               Column("birthday", String(200), default='', server_default=''),
               Column("location", String(100), default='', server_default=''),
               Column("description", String(500), default='', server_default=''),
               Column("register_time", String(200), default='', server_default=''),
               Column("verify_type", INTEGER, default=0, server_default='0'),
               Column("verify_info", String(2500), default='', server_default=''),
               Column("follows_num", INTEGER, default=0, server_default='0'),
               Column("fans_num", INTEGER, default=0, server_default='0'),
               Column("wb_num", INTEGER, default=0, server_default='0'),
               Column("level", INTEGER, default=0, server_default='0'),
               Column("tags", String(500), default='', server_default=''),
               Column("work_info", String(500), default='', server_default=''),
               Column("contact_info", String(300), default='', server_default=''),
               Column("education_info", String(300), default='', server_default=''),
               Column("head_img", String(500), default='', server_default=''),
               )

# seed ids for user crawling
seed_id = Table('seed_id', metadata,
                Column("id", INTEGER, primary_key=True, autoincrement=True),
                Column("uid", String(20), unique=True),
                Column("is_crawled", INTEGER, default=0, server_default='0'),
                Column("home_crawled", INTEGER, default=0, server_default='0'),
                Column("relation_crawled", INTEGER, default=0, server_default='0'),
            )

# relations about user and there fans and follows
relation = Table("relation", metadata,
                 Column('id', INTEGER, primary_key=True, autoincrement=True),
                 Column('user_id', String(20)),
                 Column('follow_or_fans_id', String(20)),
                 Column('type', INTEGER),  # 1 stands for fans, 2 stands for follows
                 )

# search keywords table
keyword = Table('keyword', metadata,
                Column("id", INTEGER, primary_key=True, autoincrement=True),
                Column("keyword", String(200), unique=True),
                Column("enable", INTEGER, default=1, server_default='1'),
            )

# weibo info data
wbdata = Table('wbdata', metadata,
               Column("id", INTEGER, primary_key=True, autoincrement=True),
               Column("weibo_id", String(200), unique=True),
               Column("weibo_cont", Text),
               Column("weibo_img", String(1000), default='', server_default=''),
               Column("weibo_img_path", String(1000), default='', server_default=''),
               Column("weibo_video", String(1000), default='', server_default=''),
               Column("repost_num", INTEGER, default=0, server_default='0'),
               Column("comment_num", INTEGER, default=0, server_default='0'),
               Column("praise_num", INTEGER, default=0, server_default='0'),
               Column("uid", String(20)),
               Column("is_origin", INTEGER, default=1, server_default='1'),
               Column("device", String(200), default='', server_default=''),
               Column("weibo_url", String(300), default='', server_default=''),
               Column("create_time", String(200)),
               Column("location", String(200), default='', server_default=''),
               )

# weibo task label
task_label = Table('task_label', metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("weibo_id", String(200), unique=True),
                   Column("comment_crawled", INTEGER, default=0, server_default='0'),
                   Column("repost_crawled", INTEGER, default=0, server_default='0'),
                   Column("dialogue_crawled", INTEGER, default=0, server_default='0'),
                   Column("praise_crawled", INTEGER, default=0, server_default='0'),
                   Column("image_download", INTEGER, default=0, server_default='0'),
                   )

# keywords and weibodata relationship
keyword_wbdata = Table('keyword_wbdata', metadata,
                       Column("id", INTEGER, primary_key=True, autoincrement=True),
                       Column("wb_id", String(200)),
                       Column("keyword_id", INTEGER),
                       )

# comment table
comment = Table('comment', metadata,
                Column("id", INTEGER, primary_key=True, autoincrement=True),
                Column("comment_id", String(50), unique=True),
                Column("comment_cont", Text),
                Column("weibo_id", String(200)),
                Column("user_id", String(20)),
                Column("create_time", String(200)),
                )

# praise table
praise = Table('praise', metadata,
               Column("id", INTEGER, primary_key=True, autoincrement=True),
               Column("user_id", String(20)),
               Column("weibo_id", String(200)),
               )

# repost table
repost = Table("repost", metadata,
               Column("id", INTEGER, primary_key=True, autoincrement=True),
               Column("user_id", String(20)),
               Column("user_name", String(200)),
               Column("weibo_id", String(200), unique=True),
               Column("parent_user_id", String(20)),
               Column("repost_time", String(200)),
               Column("repost_cont", Text),
               Column("weibo_url", String(200)),
               Column("parent_user_name", String(200)),
               Column("root_weibo_id", String(200)),
               )

# dialogue table
dialogue = Table("dialogue", metadata,
                 Column("id", INTEGER, primary_key=True, autoincrement=True),
                 Column("dialogue_id", String(50), unique=True),
                 Column("weibo_id", String(200)),
                 Column("dialogue_cont", Text),
                 Column("dialogue_rounds", INTEGER),
                 )