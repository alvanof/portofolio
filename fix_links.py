import sys, re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update English JS Translations
content = re.sub(r'(cc_desc1:\s*\"I produce engaging 2D animation shorts on TikTok<br><a href=)[\'\"].*?[\'\"]', r'\g<1>\'https://www.tiktok.com/@animasi.mulmul\'', content)
content = re.sub(r'(cc_desc2:\s*\"Along with longer narrative content on YouTube<br><a href=)[\'\"].*?[\'\"]', r'\g<1>\'https://www.youtube.com/@Mulmul\'', content)
content = re.sub(r'(cc_desc3:\s*\"I also experiment with AI-driven content on my personal account<br><a href=)[\'\"].*?[\'\"]', r'\g<1>\'https://www.instagram.com/alvanof_/\'', content)

# 2. Update Indonesian JS Translations
content = re.sub(r'(cc_desc1:\s*\"Saya membuat animasi 2D shorts untuk TikTok<br><a href=)[\'\"].*?[\'\"]', r'\g<1>\'https://www.tiktok.com/@animasi.mulmul\'', content)
content = re.sub(r'(cc_desc2:\s*\"Juga konteng long untuk YouTube<br><a href=)[\'\"].*?[\'\"]', r'\g<1>\'https://www.youtube.com/@Mulmul\'', content)
content = re.sub(r'(cc_desc3:\s*\"Aku juga coba membuat konten AI di akun pribadiku<br><a href=)[\'\"].*?[\'\"]', r'\g<1>\'https://www.instagram.com/alvanof_/\'', content)

# 3. Update HTML Body Hardcoded Links (by matching specific context)
content = re.sub(r'(videos<br><a href=)[\'\"].*?[\'\"]([^<]*>[\s\S]*?Animasi mulmul)', r'\g<1>"https://www.tiktok.com/@animasi.mulmul"\g<2>', content)
content = re.sub(r'(form too<br><a\s+href=)[\'\"].*?[\'\"]([^<]*>[\s\S]*?Animasi mulmul)', r'\g<1>"https://www.youtube.com/@Mulmul"\g<2>', content)
content = re.sub(r'(account<br><a href=)[\'\"].*?[\'\"]([^<]*>[\s\S]*?Mulia\s+mahendra)', r'\g<1>"https://www.instagram.com/alvanof_/"\g<2>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Links successfully updated.')
