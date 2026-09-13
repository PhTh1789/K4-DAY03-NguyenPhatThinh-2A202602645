# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Phát Thịnh
> **Mã Sinh Viên / Mã Học viên:** 2A202602645
> **Chủ đề Lựa chọn:** Đề tài Mở - Trợ lý tổng hợp thông tin và ghi chú từ các kênh Discord AI Thực Chiến

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá           | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm                                      |
| :-------------------------- | :------------: | :----------------------------------------------------------------------- |
| **1. Multi-step Reasoning** |      4 / 5       | Cần nhiều bước: truy vấn lấy tin nhắn -> suy luận lọc thông tin -> tóm tắt -> gọi tool ghi chú. |
| **2. Tool Interaction**     |      5 / 5       | Chắc chắn cần gọi 2 tool qua MCP (Tool tra cứu tin nhắn Discord và Tool ghi chú/tạo file tổng hợp). |
| **3. Dynamic Decision**     |      4 / 5       | Phải đọc xem nội dung trong kênh có gì rồi mới quyết định nội dung sẽ tổng hợp và ghi chú lại. |
| **4. Long Horizon Goal**    |      3 / 5       | Mục tiêu khá rõ ràng và được giải quyết trong 1-2 lượt gọi tool, không cần duy trì quá dài hạn. |
| **TỔNG ĐIỂM AGENTIC FIT**   |    **16 / 20**    | _Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System._ |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "gpa": 3.85
      }
    },
    "latency_ms": 120.5
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** \_\_\_ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** \_\_\_ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
