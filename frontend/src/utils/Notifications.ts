import { notification } from "antd";

export const NotificationType = {
  ERROR: "ERROR",
  INFO: "INFO",
  SUCCESS: "SUCCESS",
  WARNING: "WARNING",
};

export function openNotification(
  message: string,
  description: string,
  type: string,
) {
  switch (type) {
    case NotificationType.ERROR:
      errorNotification(message, description);
      break;
    case NotificationType.SUCCESS:
      successNotification(message, description);
      break;
    case NotificationType.WARNING:
      warningNotification(message, description);
      break;
    default:
      infoNotification(message, description);
      break;
  }
}

function errorNotification(message: string, description: string) {
  return notification.error({ message, description });
}
function successNotification(message: string, description: string) {
  return notification.success({ message, description });
}
function warningNotification(message: string, description: string) {
  return notification.warning({ message, description });
}
function infoNotification(message: string, description: string) {
  return notification.info({ message, description });
}
