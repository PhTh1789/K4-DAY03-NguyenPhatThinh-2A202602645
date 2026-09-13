# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Phát Thịnh
> **Mã Sinh Viên / Mã Học viên:** 2A202602645
> **Chủ đề Lựa chọn:** Đề tài Mở - Trợ lý tổng hợp thông tin và ghi chú từ các kênh Discord AI Thực Chiến

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá           | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm                                                                 |
| :-------------------------- | :------------: | :-------------------------------------------------------------------------------------------------- |
| **1. Multi-step Reasoning** |     4 / 5      | Cần nhiều bước: truy vấn lấy tin nhắn -> suy luận lọc thông tin -> tóm tắt -> gọi tool ghi chú.     |
| **2. Tool Interaction**     |     5 / 5      | Chắc chắn cần gọi 2 tool qua MCP (Tool tra cứu tin nhắn Discord và Tool ghi chú/tạo file tổng hợp). |
| **3. Dynamic Decision**     |     4 / 5      | Phải đọc xem nội dung trong kênh có gì rồi mới quyết định nội dung sẽ tổng hợp và ghi chú lại.      |
| **4. Long Horizon Goal**    |     3 / 5      | Mục tiêu khá rõ ràng và được giải quyết trong 1-2 lượt gọi tool, không cần duy trì quá dài hạn.     |
| **TỔNG ĐIỂM AGENTIC FIT**   |  **16 / 20**   | _Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System._                            |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Tổng hợp các câu hỏi trong kênh #hoidap rồi lưu vào file các điều cần lưu ý.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "fetch_discord_messages",
    "arguments": {
      "limit": 20,
      "channel_name": "hoidap"
    },
    "observation": {
      "status": "SUCCESS",
      "channel": "hoidap",
      "data": [
        {
          "author": "SV01",
          "content": "Cho em hỏi tool schema là gì ạ?",
          "timestamp": "2026-09-13T10:00:00Z"
        },
        {
          "author": "Labcoachs",
          "content": "Là một định dạng JSON mô tả công cụ cho LLM hiểu em nhé.",
          "timestamp": "2026-09-13T10:15:00Z"
        }
      ]
    },
    "latency_ms": 2384.77
  },
  {
    "step": 2,
    "query": "Tổng hợp các câu hỏi trong kênh #hoidap rồi lưu vào file các điều cần lưu ý.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Đã lấy được dữ liệu thành công:\n[\n  {\n    \"author\": \"SV01\",\n    \"content\": \"Cho em hỏi tool schema là gì ạ?\",\n    \"timestamp\": \"2026-09-13T10:00:00Z\"\n  },\n  {\n    \"author\": \"Labcoachs\",\n    \"content\": \"Là một định dạng JSON mô tả công cụ cho LLM hiểu em nhé.\",\n    \"timestamp\": \"2026-09-13T10:15:00Z\"\n  }\n]",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 5 lượt.
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
