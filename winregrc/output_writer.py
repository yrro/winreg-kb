# -*- coding: utf-8 -*-
"""Output writer."""

from __future__ import print_function
from __future__ import unicode_literals

import abc

from winregrc import hexdump


class OutputWriter(object):
  """Output writer interface."""

  @abc.abstractmethod
  def Close(self):
    """Closes the output writer."""

  @abc.abstractmethod
  def Open(self):
    """Opens the output writer.

    Returns:
      bool: True if successful or False if not.
    """

  @abc.abstractmethod
  def WriteDebugData(self, description, data):
    """Writes data for debugging.

    Args:
      description (str): description to write.
      data (bytes): data to write.
    """

  @abc.abstractmethod
  def WriteIntegerValueAsDecimal(self, description, value):
    """Writes an integer value as decimal for debugging.

    Args:
      description (str): description to write.
      value (int): value to write.
    """

  @abc.abstractmethod
  def WriteValue(self, description, value):
    """Writes a value for debugging.

    Args:
      description (str): description to write.
      value (str): value to write.
    """

  @abc.abstractmethod
  def WriteText(self, text):
    """Writes text for debugging.

    Args:
      text (str): text to write.
    """


class StdoutOutputWriter(OutputWriter):
  """Stdout output writer."""

  def Close(self):
    """Closes the output writer."""
    pass

  def Open(self):
    """Opens the output writer.

    Returns:
      bool: True if successful or False if not.
    """
    return True

  def WriteDebugData(self, description, data):
    """Writes data for debugging.

    Args:
      description (str): description to write.
      data (bytes): data to write.
    """
    self.WriteText(description)

    hexdump_text = hexdump.Hexdump(data)
    self.WriteText(hexdump_text)

  def WriteIntegerValueAsDecimal(self, description, value):
    """Writes an integer value as decimal for debugging.

    Args:
      description (str): description to write.
      value (int): value to write.
    """
    value_string = '{0:d}'.format(value)
    self.WriteValue(description, value_string)

  def WriteValue(self, description, value):
    """Writes a value for debugging.

    Args:
      description (str): description to write.
      value (object): value to write.
    """
    description_no_tabs = description.replace('\t', ' ' * 8)
    alignment, _ = divmod(len(description_no_tabs), 8)
    alignment = 8 - alignment + 1
    text = '{0:s}{1:s}: {2!s}'.format(description, '\t' * alignment, value)
    self.WriteText(text)

  def WriteText(self, text):
    """Writes text for debugging.

    Args:
      text (str): text to write.
    """
    text = text.encode('utf8')
    print(text)
