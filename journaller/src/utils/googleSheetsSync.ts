import { ClassData } from '../types/gradebook';

export type SyncStatus = 'disconnected' | 'connected' | 'syncing' | 'synced' | 'error';

const WEBHOOK_KEY = 'journaller_sheets_webhook_url';
const AUTO_SYNC_KEY = 'journaller_sheets_auto_sync_enabled';

export function getSavedWebhookUrl(): string {
  return localStorage.getItem(WEBHOOK_KEY) || '';
}

export function saveWebhookUrl(url: string) {
  localStorage.setItem(WEBHOOK_KEY, url.trim());
}

export function getAutoSyncEnabled(): boolean {
  const val = localStorage.getItem(AUTO_SYNC_KEY);
  return val === null ? true : val === 'true';
}

export function setAutoSyncEnabled(enabled: boolean) {
  localStorage.setItem(AUTO_SYNC_KEY, String(enabled));
}

/**
 * Test connectivity with the Google Apps Script Web App.
 */
export async function testWebhookConnection(url: string): Promise<{ success: boolean; message: string; sheetTitle?: string }> {
  if (!url || !url.startsWith('https://script.google.com/')) {
    return {
      success: false,
      message: 'URL must start with https://script.google.com/macros/s/.../exec',
    };
  }

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'text/plain;charset=utf-8',
      },
      body: JSON.stringify({ action: 'test_connection' }),
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const data = await response.json();
    if (data.status === 'success') {
      return {
        success: true,
        message: data.message || 'Connected successfully!',
        sheetTitle: data.sheetTitle,
      };
    } else {
      return {
        success: false,
        message: data.message || 'Google Sheets responded with an error',
      };
    }
  } catch (err: any) {
    return {
      success: false,
      message: err.message || 'Failed to connect to Google Sheets Web App',
    };
  }
}

/**
 * Sends real-time class data to Google Sheets.
 */
export async function syncClassToGoogleSheets(
  classData: ClassData,
  customUrl?: string
): Promise<{ success: boolean; message: string; timestamp: Date }> {
  const url = customUrl || getSavedWebhookUrl();

  if (!url) {
    return {
      success: false,
      message: 'No Google Sheets Web App URL configured',
      timestamp: new Date(),
    };
  }

  try {
    const payload = {
      action: 'sync_all',
      classData,
    };

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'text/plain;charset=utf-8',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`HTTP error ${response.status}`);
    }

    const result = await response.json();
    if (result.status === 'success') {
      return {
        success: true,
        message: result.message || 'Saved to Google Sheets',
        timestamp: new Date(),
      };
    } else {
      throw new Error(result.message || 'Google Sheet update failed');
    }
  } catch (err: any) {
    return {
      success: false,
      message: err.message || 'Network error saving to Google Sheets',
      timestamp: new Date(),
    };
  }
}

/**
 * Creates a debounced auto-sync dispatcher.
 */
export function createDebouncedSync(delayMs = 800) {
  let timer: any = null;

  return function queueSync(
    classData: ClassData,
    onStatusChange: (status: SyncStatus, msg?: string, time?: Date) => void
  ) {
    const url = getSavedWebhookUrl();
    const enabled = getAutoSyncEnabled();

    if (!url || !enabled) {
      onStatusChange(url ? 'connected' : 'disconnected');
      return;
    }

    onStatusChange('syncing', 'Saving to Google Sheet...');

    if (timer) clearTimeout(timer);

    timer = setTimeout(async () => {
      const res = await syncClassToGoogleSheets(classData, url);
      if (res.success) {
        onStatusChange('synced', res.message, res.timestamp);
      } else {
        onStatusChange('error', res.message, res.timestamp);
      }
    }, delayMs);
  };
}
