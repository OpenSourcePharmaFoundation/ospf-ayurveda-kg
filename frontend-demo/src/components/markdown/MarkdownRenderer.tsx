import { useMemo } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeRaw from 'rehype-raw';
import rehypeSanitize from 'rehype-sanitize';
import { preprocessMarkdown } from '@/lib/markdown-preprocessor';
import type { Components } from 'react-markdown';

const sanitizeSchema = {
  tagNames: [
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'p', 'a', 'ul', 'ol', 'li', 'blockquote',
    'pre', 'code', 'em', 'strong', 'del',
    'table', 'thead', 'tbody', 'tr', 'th', 'td',
    'hr', 'br', 'div', 'span', 'img', 'sup', 'sub',
  ],
  attributes: {
    '*': ['className', 'class', 'style', 'title', 'id'],
    a: ['href', 'target', 'rel'],
    img: ['src', 'alt', 'width', 'height'],
    td: ['colSpan', 'rowSpan'],
    th: ['colSpan', 'rowSpan'],
  },
};

const customComponents: Components = {
  table: ({ children }) => (
    <div className="overflow-x-auto my-4 rounded-lg border border-border">
      <table className="min-w-full text-sm">{children}</table>
    </div>
  ),
  thead: ({ children }) => (
    <thead className="bg-muted/50 text-xs uppercase tracking-wider text-muted-foreground">
      {children}
    </thead>
  ),
  th: ({ children }) => (
    <th className="px-2 sm:px-4 py-2 sm:py-3 text-left font-semibold border-b border-border">
      {children}
    </th>
  ),
  td: ({ children }) => (
    <td className="px-2 sm:px-4 py-2 sm:py-2.5 border-b border-border/50">{children}</td>
  ),
  tr: ({ children }) => <tr className="hover:bg-muted/30 transition-colors">{children}</tr>,
  h1: ({ children }) => (
    <h1 className="text-xl sm:text-2xl font-bold text-foreground mt-6 sm:mt-8 mb-3 sm:mb-4 pb-2 border-b-2 border-primary/30">
      {children}
    </h1>
  ),
  h2: ({ children }) => (
    <h2 className="text-lg sm:text-xl font-semibold text-foreground mt-6 sm:mt-8 mb-2 sm:mb-3 pb-1 border-b border-border">
      {children}
    </h2>
  ),
  h3: ({ children }) => (
    <h3 className="text-lg font-medium text-foreground mt-5 mb-2">{children}</h3>
  ),
  h4: ({ children }) => (
    <h4 className="text-base font-medium text-foreground mt-4 mb-1.5">{children}</h4>
  ),
  code: ({ className, children, ...props }) => {
    const isInline = !className;
    if (isInline) {
      return (
        <code
          className="bg-muted text-primary px-1.5 py-0.5 rounded text-sm font-mono"
          {...props}
        >
          {children}
        </code>
      );
    }
    return (
      <pre className="bg-card border border-border p-4 rounded-lg my-4 overflow-x-auto text-sm font-mono leading-relaxed">
        <code className={className} {...props}>
          {children}
        </code>
      </pre>
    );
  },
  blockquote: ({ children }) => (
    <blockquote className="border-l-4 border-primary/40 bg-primary/5 pl-4 py-2 my-4 rounded-r-lg text-muted-foreground">
      {children}
    </blockquote>
  ),
  a: ({ href, children }) => (
    <a
      href={href}
      className="text-primary hover:text-primary/80 underline decoration-primary/30 hover:decoration-primary/60"
      target="_blank"
      rel="noopener noreferrer"
    >
      {children}
    </a>
  ),
  ul: ({ children }) => (
    <ul className="list-disc list-outside ml-6 my-3 space-y-1 text-foreground/80">
      {children}
    </ul>
  ),
  ol: ({ children }) => (
    <ol className="list-decimal list-outside ml-6 my-3 space-y-1 text-foreground/80">
      {children}
    </ol>
  ),
  li: ({ children }) => <li className="leading-relaxed">{children}</li>,
  hr: () => <hr className="my-6 border-t border-border" />,
  p: ({ children }) => <p className="my-2 leading-relaxed text-foreground/80">{children}</p>,
  strong: ({ children }) => <strong className="font-semibold text-foreground">{children}</strong>,
};

interface MarkdownRendererProps {
  content: string;
  className?: string;
}

export function MarkdownRenderer({ content, className = '' }: MarkdownRendererProps) {
  const processed = useMemo(() => preprocessMarkdown(content), [content]);

  return (
    <article className={`max-w-none ${className}`}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeRaw, [rehypeSanitize, sanitizeSchema]]}
        components={customComponents}
      >
        {processed}
      </ReactMarkdown>
    </article>
  );
}
