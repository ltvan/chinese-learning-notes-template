# Ghi chú học tiếng Hoa — vault mẫu

Khung sườn cho một vault ghi chú tiếng Hoa cá nhân, dành cho người Việt: bạn học trên app nào cũng được, rồi đưa danh sách chữ/từ vừa học cho một **AI agent** (Claude, ChatGPT/Codex, Gemini/Antigravity, Copilot, Cursor…) — agent viết note cho từng từ, từng chữ, từng bộ thủ (cấu tạo, mẹo nhớ, âm Hán Việt, phồn thể, chữ dễ nhầm), liên kết chúng với nhau và sinh chỉ mục tra cứu. Tất cả là file Markdown thuần nằm trên máy bạn, đọc bằng [Obsidian](https://obsidian.md) hoặc VS Code.

Repo kèm sẵn một buổi học mẫu ([[2026-09-20]]: chào hỏi, cảm ơn, xin lỗi) để bạn thấy note trông ra sao.

## Bắt đầu

### 1. Lấy vault về máy

Chọn một trong ba cách:

- **Download ZIP** (dễ nhất, không cần biết Git): trên [trang GitHub của repo này](https://github.com/ltvan/chinese-learning-notes-template) bấm nút **Code → Download ZIP**, giải nén vào nơi bạn muốn lưu (vd `Documents/tieng-hoa`).
- **Fork / Use this template**: nếu bạn có tài khoản GitHub và muốn lưu vault của mình trên đó — bấm **Fork** (hoặc **Use this template**), rồi clone repo của bạn về máy.
- **Clone**: `git clone https://github.com/ltvan/chinese-learning-notes-template.git`.

### 2. Mở bằng Obsidian

1. Cài [Obsidian](https://obsidian.md) (miễn phí).
2. Mở Obsidian → **Open folder as vault** → chọn thư mục vừa giải nén/clone.
3. Cấu hình đi kèm sẵn trong `.obsidian/`, không cần cài plugin nào: template nằm ở `templates/`, Daily note tạo nhật ký buổi học trong `lessons/`.
4. Mẹo dùng:
   - Bấm vào `[[liên kết]]` để nhảy giữa từ ↔ chữ ↔ bộ thủ; mở panel **Backlinks** ở note một bộ thủ để thấy mọi chữ đã học chứa bộ đó.
   - **Graph view** cho thấy mạng lưới chữ – từ – bộ thủ bạn đã học.
   - **Search** (Ctrl/Cmd+Shift+F): gõ `hao3`, `hảo` hoặc nghĩa tiếng Việt.

Không thích Obsidian? Mở thư mục bằng VS Code với một extension hỗ trợ wikilink — [Markdown Wiki Links](https://marketplace.visualstudio.com/items?itemName=ltvan.markdown-wiki-links) (`ltvan.markdown-wiki-links`) hoặc [Foam](https://marketplace.visualstudio.com/items?itemName=foam.foam-vscode) — cũng được.

### 3. Kết nối AI agent

Agent là người viết note. Dùng bất cứ agent nào đọc/ghi được file trong thư mục vault và chạy được lệnh — toàn bộ quy ước nằm trong `AGENTS.md`, chuẩn chung mà hầu hết agent tự nạp:

- **Claude Cowork** (trong app Claude Desktop — hợp với người không rành kỹ thuật): mở Cowork, chọn thư mục vault làm thư mục làm việc.
- **[Claude Code](https://claude.com/claude-code)** (terminal, VS Code hoặc app desktop): mở trong thư mục vault — `CLAUDE.md` được nạp tự động và trỏ sang `AGENTS.md`.
- **ChatGPT → [Codex](https://openai.com/codex/)**: Codex là agent của OpenAI, dùng chung tài khoản ChatGPT. App ChatGPT thông thường chỉ trò chuyện, không sửa được file trên máy bạn — hãy cài app Codex cho desktop (hoặc Codex CLI / extension VS Code), rồi mở thư mục vault trong đó.
- **Gemini → [Antigravity](https://antigravity.google/)**: Antigravity là app agent cho desktop của Google, chạy bằng Gemini và đăng nhập bằng tài khoản Google. Trang gemini.google.com chỉ trò chuyện — hãy cài Antigravity (hoặc Gemini CLI), rồi mở thư mục vault trong đó.
- **Agent khác** (GitHub Copilot, Cursor…): mở trong thư mục vault; đa số tự đọc `AGENTS.md`.

Nếu không chắc agent của bạn có tự nạp hay không, ở tin nhắn đầu tiên cứ bảo: _"đọc AGENTS.md và làm theo quy ước trong đó"_.

Cứ sửa `AGENTS.md` cho hợp với bạn (học phồn thể là chính, ghi chú bằng ngôn ngữ khác…). Nếu bạn không dùng Git, bảo agent bỏ qua bước commit.

Agent cần **Python 3** trên máy để sinh chỉ mục (`python3 tools/build_index.py`). `npx` (Node.js) là tuỳ chọn, chỉ để format bằng Prettier.

### 4. Dọn note mẫu (tuỳ chọn)

Muốn bắt đầu từ vault trống, bảo agent: _"xoá toàn bộ note mẫu trong chars, words, radicals, confusables, lessons rồi sinh lại index"_. Muốn giữ làm ví dụ thì cứ để nguyên.

## Tra cứu

- [[by-pinyin]] — theo pinyin
- [[by-hanviet]] — theo âm Hán Việt
- [[by-radical]] — theo bộ thủ
- [[by-date]] — theo ngày học
- [[traditional]] — tra ngược từ chữ phồn thể
- Search nhanh: gõ `hao3` (pinyin không dấu), `hảo` (Hán Việt) hoặc nghĩa tiếng Việt — đều nằm trong frontmatter.
- Mở note một bộ thủ (vd [[女]]) và xem **backlink** → mọi chữ đã học chứa bộ đó.

## Cách dùng hằng ngày

1. Học xong trên app → dán chữ/từ vào [[inbox]] (hoặc gõ thẳng cho agent: "hôm nay học 你好, 谢谢").
2. Bảo agent "xử lý inbox" → agent viết note từ, chữ, bộ thủ, nhật ký buổi học, cập nhật chỉ mục, commit.
3. Muốn thêm ý riêng: viết vào mục **Ghi chú của tôi** của note — agent không đụng vào mục này.
4. Ôn: "quiz tôi các chữ tuần này" / "quiz nhóm chữ dễ nhầm".

## Cấu trúc

| Folder         | Nội dung                                              |
| -------------- | ----------------------------------------------------- |
| `chars/`       | mỗi chữ Hán một note                                  |
| `words/`       | mỗi từ ghép một note, link về từng chữ                |
| `radicals/`    | bộ thủ và thành phần (kể cả biến thể như 亻)          |
| `confusables/` | nhóm chữ dễ nhầm                                      |
| `grammar/`     | mẫu câu, ngữ pháp                                     |
| `lessons/`     | nhật ký từng buổi học                                 |
| `index/`       | chỉ mục sinh tự động — `python3 tools/build_index.py` |
| `templates/`   | khuôn note                                            |

Quy ước chi tiết cho agent: `AGENTS.md`.

## Giấy phép

[MIT](LICENSE) — dùng, sửa, chia sẻ thoải mái.
