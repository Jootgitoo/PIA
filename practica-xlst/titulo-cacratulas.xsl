<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/albumes">
    <html lang="es">

      <head>
        <meta charset="UTF-8"/>
        <title>Titulo del album + caratulas</title>
      </head>

      <body>
        <h2>Título del álbum + carátulas</h2>

        <xsl:for-each select="album">

          <div style="margin-bottom: 20px;">
            <p>Título: <xsl:value-of select="titulo"/></p>
            <img src="{imagen}" alt="{titulo}" width="200"/>
          </div>
          
        </xsl:for-each>

      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
