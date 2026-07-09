-- ==========================================================
-- Question 2 - SQL & Data Modeling
-- Trafasa Technology Round 1 Assessment
-- ==========================================================

-- Create Purchase Order Items table
CREATE TABLE po_items (
    po_id VARCHAR(20),
    item_code VARCHAR(20),
    quantity_ordered INT
);

-- Create Goods Received Note Items table
CREATE TABLE grn_items (
    grn_id VARCHAR(20),
    po_id VARCHAR(20),
    item_code VARCHAR(20),
    quantity_received INT
);

-- Sample Data
INSERT INTO po_items (po_id, item_code, quantity_ordered) VALUES
('PO-2024-001', 'ITEM001', 100),
('PO-2024-001', 'ITEM002', 150);

INSERT INTO grn_items (grn_id, po_id, item_code, quantity_received) VALUES
('GRN001', 'PO-2024-001', 'ITEM001', 60),
('GRN002', 'PO-2024-001', 'ITEM001', 40),
('GRN003', 'PO-2024-001', 'ITEM002', 150);

-- SQL Query to calculate the total quantity received
SELECT
    po_id,
    SUM(quantity_received) AS total_quantity_received
FROM grn_items
WHERE po_id = 'PO-2024-001'
GROUP BY po_id;