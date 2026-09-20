# Vault ghi chú tiếng Hoa

Vault cá nhân ghi lại những gì người dùng đã học tiếng Hoa trên app bên ngoài. Người dùng là người Việt,
đang học **giản thể**, ghi kèm **phồn thể** khi thú vị. Note viết bằng tiếng Việt. Người dùng đưa danh sách chữ/từ,
AI agent viết note. Đọc bằng cả VS Code (wikilink extension) lẫn Obsidian → không phụ thuộc plugin.

## Quy tắc cứng

1. **Mỗi ký tự/từ có đúng 1 file trong cả vault**, tên file là chính nó (`好.md`, `你好.md`). Trước khi tạo, kiểm tra cả `chars/`, `words/`, `radicals/`.
2. **Đặt file ở đâu:**
   - 214 bộ thủ Khang Hy và biến thể của chúng (亻氵扌…) → `radicals/`, kể cả khi nó cũng là chữ thường (女, 水, 人). Khi người dùng học nó như một chữ: `type: [radical, char]`, thêm `learned`, bổ sung nghĩa/từ ghép.
   - Chữ khác → `chars/`. Từ ≥ 2 chữ → `words/`.
   - Biến thể bộ thủ có file riêng với `variant_of: <bộ gốc>`.
3. **Mọi thứ trong `components`, `radical`, `chars`, `variant_of` phải có note.** Thành phần là chữ chưa học → tạo stub trong `chars/` (`status: stub`, KHÔNG có `learned`, thân note 1–2 dòng). Khi sau này học tới, bỏ `status`, thêm `learned`, viết đầy đủ.
4. **`learned` chỉ ghi khi người dùng thực sự đã học** chữ/từ đó (ngày dạng YYYY-MM-DD). Index chỉ liệt kê note có `learned`.
5. **Không ghi đè mục "Ghi chú của tôi"** và bất cứ thứ gì người dùng tự viết. Khi cập nhật note cũ, chỉ bổ sung.
6. **Frontmatter phẳng**: `key: value` hoặc `key: [a, b]`; giá trị chứa `: ` thì bọc ngoặc kép. Script index không đọc YAML lồng nhau.
7. `index/` là file sinh tự động — không sửa tay, chạy `python3 tools/build_index.py`.
8. Không chắc về từ nguyên/cấu tạo thì nói rõ là "mẹo nhớ" chứ không khẳng định là từ nguyên. Pinyin, Hán Việt, bộ thủ phải chính xác.
9. **Viết đúng chuẩn Prettier** (`.prettierrc`; `index/` và `templates/` được bỏ qua) để format-on-save không sinh diff: dòng trống sau frontmatter và quanh heading/list/bảng, nghiêng dùng `_x_` (không dùng `*x*`), đậm dùng `**x**`, list dùng `-`. Mỗi trường `**Nhãn:** …` trong thân note là một đoạn riêng, cách nhau bằng dòng trống (Markdown chuẩn/VS Code preview gộp các dòng liền nhau thành một đoạn). Nếu có `npx`, chạy `npx -y prettier@3 --write .` trước khi commit.

## Nội dung note

Dùng template trong `templates/`. Những điểm tạo giá trị ghi nhớ — luôn cố gắng có:

- **Cấu tạo**: loại chữ (tượng hình / chỉ sự / hội ý / hình thanh). Với hình thanh ghi rõ phần **gợi nghĩa** và phần **gợi âm**, wikilink tới từng thành phần.
- **Mẹo nhớ**: một câu chuyện ngắn gắn các thành phần với nghĩa.
- **Hán Việt**: luôn ghi; nêu từ Hán Việt quen thuộc trong tiếng Việt có chữ này (好 hảo → "hảo hạng", "hữu hảo").
- **Phồn thể**: nếu khác giản thể, ghi `traditional` + `aliases` trong frontmatter, và mục "Phồn thể" phân tích chữ phồn thể nói thêm được gì (愛 có 心). Giống nhau thì ghi "giống giản thể".
- **Từ ghép**: wikilink tới các từ đã có note; cập nhật khi thêm từ mới chứa chữ này.
- **Dễ nhầm với**: khi chữ mới na ná chữ **đã học** → tạo/cập nhật note trong `confusables/` (tên file nối bằng `-`: `己-已-巳.md`) và link hai chiều.
- `pinyin_plain`: không dấu + số thanh, viết liền (`hao3`, `ni3hao3`; thanh nhẹ là `5`). Chữ đa âm: `pinyin` ghi âm chính đã học, các âm khác ghi trong thân note.

## Workflow "buổi học mới"

Khi người dùng đưa danh sách chữ/từ (trong chat hoặc trong `inbox.md`):

1. Với mỗi từ: tạo/cập nhật `words/`, rồi từng chữ trong đó, rồi bộ thủ/thành phần còn thiếu (stub nếu cần).
2. Cập nhật mục "Từ ghép" ở các note chữ liên quan đã tồn tại.
3. Rà chữ dễ nhầm với chữ đã học → `confusables/`.
4. Ghi/cập nhật `lessons/YYYY-MM-DD.md` (link tới mọi thứ mới của buổi đó, kèm ghi chú người dùng đưa).
5. Chạy `python3 tools/build_index.py` — phải exit 0, không cảnh báo.
6. Xoá các dòng đã xử lý khỏi `inbox.md` (giữ phần hướng dẫn đầu file).
7. Commit: `lesson YYYY-MM-DD: +N words, +M chars`. Một nhánh duy nhất, không push trừ khi được yêu cầu.

## Các yêu cầu khác

- **Tìm chữ** ("chữ gì có bộ thủy nghĩa là sông"): tìm trong frontmatter (`radical`, `components`, `meaning`, `hanviet`, `pinyin_plain`) và `index/`.
- **Quiz/ôn tập**: lấy từ `lessons/` gần đây hoặc `confusables/`; hỏi từng câu một, không lộ đáp án trước.
- **Ngữ pháp/mẫu câu** → `grammar/`, tên file là mẫu câu (`把字句.md`), ví dụ wikilink tới từ đã học.
