import * as React from 'react';
import { Drawer as DrawerPrimitive } from '@base-ui/react/drawer';
import { X } from 'lucide-react';
import { cn } from '@/lib/utils';

const Drawer = DrawerPrimitive.Root;
const DrawerTrigger = DrawerPrimitive.Trigger;
const DrawerClose = DrawerPrimitive.Close;
const DrawerTitle = DrawerPrimitive.Title;
const DrawerDescription = DrawerPrimitive.Description;

function DrawerBackdrop({
  className,
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Backdrop>) {
  return (
    <DrawerPrimitive.Backdrop
      className={cn(
        'fixed inset-0 z-40 bg-black/40 transition-opacity duration-300',
        'data-[ending-style]:opacity-0 data-[starting-style]:opacity-0',
        className,
      )}
      {...props}
    />
  );
}

function DrawerContent({
  className,
  children,
  title,
  description,
  ...props
}: React.ComponentProps<typeof DrawerPrimitive.Popup> & {
  title?: string;
  description?: string;
}) {
  return (
    <DrawerPrimitive.Portal>
      <DrawerBackdrop />
      <DrawerPrimitive.Popup
        className={cn(
          'fixed inset-y-0 right-0 z-50 flex w-full max-w-md flex-col bg-card shadow-xl transition-transform duration-300 ease-out',
          'data-[ending-style]:translate-x-full data-[starting-style]:translate-x-full',
          className,
        )}
        {...props}
      >
        <div className="flex items-start justify-between border-b border-border px-6 py-4">
          <div className="min-w-0 pr-4">
            {title && (
              <DrawerPrimitive.Title className="text-lg font-semibold text-foreground truncate">
                {title}
              </DrawerPrimitive.Title>
            )}
            {description && (
              <DrawerPrimitive.Description className="text-sm text-muted-foreground mt-0.5">
                {description}
              </DrawerPrimitive.Description>
            )}
          </div>
          <DrawerPrimitive.Close className="shrink-0 rounded-md p-1.5 text-muted-foreground hover:text-foreground hover:bg-muted transition-colors">
            <X className="size-4" />
          </DrawerPrimitive.Close>
        </div>
        <div className="flex-1 overflow-y-auto">{children}</div>
      </DrawerPrimitive.Popup>
    </DrawerPrimitive.Portal>
  );
}

export {
  Drawer,
  DrawerTrigger,
  DrawerClose,
  DrawerContent,
  DrawerTitle,
  DrawerDescription,
  DrawerBackdrop,
};
