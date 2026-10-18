import React, { useEffect, useMemo, useState } from "react";
import "./SelectItem.css";

export type SelectableItem = {
  id: string;
  label: string;
  type: "full" | "empty";
};

export type SelectItemProps = {
  items?: SelectableItem[];
  initialSelectedIds?: string[];
  onClose?: () => void;
  onSelectionChange?: (selectedIds: string[]) => void;
};

const DEFAULT_ITEMS: SelectableItem[] = [
  { id: "400ml-coke", label: "400MLPBTN1X24 Coke 150M", type: "full" },
  { id: "750ml-kinley", label: "750MLPBTN1X24 Kinley", type: "full" },
];

export function SelectItem({
  items = DEFAULT_ITEMS,
  initialSelectedIds = ["400ml-coke"],
  onClose,
  onSelectionChange,
}: SelectItemProps) {
  const [activeType, setActiveType] = useState<SelectableItem["type"]>("full");
  const [query, setQuery] = useState("");
  const [selectedIds, setSelectedIds] = useState<string[]>(initialSelectedIds);
  const [isOpen, setIsOpen] = useState(true);

  useEffect(() => {
    function handleKeyDown(event: KeyboardEvent) {
      if (event.key === "Escape") {
        setIsOpen(false);
        onClose?.();
      }
    }

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [onClose]);

  const visibleItems = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase();
    return items.filter(
      (item) =>
        item.type === activeType &&
        item.label.toLowerCase().includes(normalizedQuery),
    );
  }, [activeType, items, query]);

  function toggleItem(id: string) {
    const nextSelectedIds = selectedIds.includes(id)
      ? selectedIds.filter((selectedId) => selectedId !== id)
      : [...selectedIds, id];

    setSelectedIds(nextSelectedIds);
    onSelectionChange?.(nextSelectedIds);
  }

  function closeDialog() {
    setIsOpen(false);
    onClose?.();
  }

  if (!isOpen) return null;

  return (
    <div className="select-item-backdrop">
      <section
        aria-labelledby="select-item-title"
        aria-modal="true"
        className="select-item-dialog"
        role="dialog"
      >
        <header className="select-item-header">
          <h1 id="select-item-title">Select Item</h1>
          <button
            aria-label="Close item selection"
            className="select-item-close"
            onClick={closeDialog}
            type="button"
          >
            <svg aria-hidden="true" viewBox="0 0 24 24">
              <path d="m8 8 8 8M16 8l-8 8" />
            </svg>
          </button>
        </header>

        <label className="select-item-search">
          <span className="select-item-visually-hidden">Search by item</span>
          <input
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Search by Item..."
            type="search"
            value={query}
          />
          <svg aria-hidden="true" className="select-item-search-icon" viewBox="0 0 32 32">
            <circle cx="14" cy="14" r="11.5" />
            <path d="m22.5 22.5 6 6" />
          </svg>
        </label>

        <div aria-label="Item type" className="select-item-tabs" role="group">
          {(["full", "empty"] as const).map((type) => (
            <button
              aria-pressed={activeType === type}
              className={`select-item-tab${activeType === type ? " is-active" : ""}`}
              key={type}
              onClick={() => setActiveType(type)}
              type="button"
            >
              {type === "full" ? "Fulls" : "Empties"}
            </button>
          ))}
        </div>

        <ul aria-label="Items" className="select-item-list">
          {visibleItems.map((item) => {
            const checked = selectedIds.includes(item.id);
            return (
              <li className="select-item-row" key={item.id}>
                <button
                  aria-checked={checked}
                  className={`select-item-checkbox${checked ? " is-checked" : ""}`}
                  onClick={() => toggleItem(item.id)}
                  role="checkbox"
                  type="button"
                >
                  {checked && (
                    <svg aria-hidden="true" viewBox="0 0 20 20">
                      <path d="m4 10 4 4 8-8" />
                    </svg>
                  )}
                </button>
                <span>{item.label}</span>
              </li>
            );
          })}
          {visibleItems.length === 0 && (
            <li aria-live="polite" className="select-item-empty-state">
              No items found.
            </li>
          )}
        </ul>
      </section>
    </div>
  );
}
